
iteraciones = 1;

connectedRadios = findsdru;
platform = connectedRadios(1).Platform;
fmRxParams = getParamsSdruFMExamples(platform)

num_mediciones = input("¿Cuantas medidas va a realizar?");

angles = 0:2*pi/(num_mediciones-1):2*pi;
powerdbm = zeros(1, num_mediciones);

centerFreq = input("¿Que frecuencia desea sintonizar en MHz?\n");

while true
    
    in = input("Presione enter para continuar.");
    
    

    radio = comm.SDRuReceiver(...
          'Platform', 'B210', ...
          'SerialNum', '30F40F4', ...
          'MasterClockRate', fmRxParams.RadioMasterClockRate);


    

    radio.CenterFrequency  = centerFreq*(10^6);
    radio.Gain = fmRxParams.RadioGain;
    radio.DecimationFactor = fmRxParams.RadioDecimationFactor;
    radio.SamplesPerFrame = fmRxParams.RadioFrameLength;
    radio.OutputDataType = 'single';

    

    for index = iteraciones: num_mediciones
            %302.9 enlace unicauca 94.1 policia 91.7autonoma
            signal = 0;
            len = 0;

            question = input(index+"° medida a realizar.\n 0 -> Realizar medida.\n 1 -> Calibrar.\n");
            
            if question 
                break
            end
            
            timeCounter = 0;
            while timeCounter < fmRxParams.StopTime
                [signal, len] = step(radio);
                if len > 0
                  % Update counter
                  timeCounter = timeCounter + fmRxParams.AudioFrameTime;
                end
            end
            
            
            if index == 1
                signals = zeros(size(signal));
            end
            signals = [signals, signal];
            
            


    end
    
    release(radio)
    iteraciones = index;
    
    if index == num_mediciones
        break
    end
    


end

signals(:,1) = [];

fechadoc = datestr(datetime('now'));
fechadoc = strrep(fechadoc,'-','_');
fechadoc = strrep(fechadoc,' ','_');
fechadoc = strrep(fechadoc,':','_');
namedoc = strcat(fechadoc,'signals','.mat');
save(namedoc,'signals')

Fs = 200e3; 
filtertype = 'FIR';
Fpass = 51e3;
Fstop = 55e3; 
Rp = 0.1;
Astop = 80;
FIRLPF = dsp.LowpassFilter('SampleRate',Fs, ...
                           'FilterType',filtertype, ...
                           'PassbandFrequency',Fpass, ...
                           'StopbandFrequency',Fstop, ...
                           'PassbandRipple',Rp, ...
                           'StopbandAttenuation',Astop);


filtertypehp = 'FIR';
Fpasshp = 49e3;
Fstophp = 45e3; 
Rphp = 0.1;
Astophp = 80;
FIRHPF = dsp.HighpassFilter('SampleRate',Fs,...
                            'FilterType',filtertypehp,...
                            'PassbandFrequency',Fpasshp,...
                            'StopbandFrequency',Fstophp,...
                            'PassbandRipple',Rphp,...
                            'StopbandAttenuation',Astophp);

for index2 = 1:num_mediciones
    
    scope = dsp.SpectrumAnalyzer;

    filteredsignalhp = FIRHPF(signals(:,index2));
    filteredsignallp = FIRLPF(filteredsignalhp);
    scope.SampleRate = Fs;
    scope(filteredsignallp)       
    spectrumData = cell2mat(getSpectrumData(scope).Spectrum);
    powerTonedbm = max(spectrumData) %potencia en dbm


    powerdbm(index2) = powerTonedbm;
    
end

%     powerAPonderar = signal.*conj(signal);
%     power_measured = mean(powerAPonderar);
%     powerindB = 10*log10(power_measured)
%     power(index) = power_measured;
%     exportar=signal;



powerdbm;
powerdbm(1) = powerdbm(length(powerdbm));
power = 10.^(powerdbm/10);
powerNormalized = power/max(power);

fechadoc1 = datestr(datetime('now'));
fechadoc1 = strrep(fechadoc1,'-','_');
fechadoc1 = strrep(fechadoc1,' ','_');
fechadoc1 = strrep(fechadoc1,':','_');
namedoc1 = strcat(fechadoc1,'pattern.fig');

figure
polarplot(angles, powerNormalized)
savefig(namedoc1)

fechadoc2 = datestr(datetime('now'));
fechadoc2 = strrep(fechadoc2,'-','_');
fechadoc2 = strrep(fechadoc2,' ','_');
fechadoc2 = strrep(fechadoc2,':','_');
namedoc2 = strcat(fechadoc2,'powers','.mat');
save(namedoc2,'powerdbm')



%save('FileName.mat','exportar')
%hola=load('FileName.mat')
%hola.exportar
