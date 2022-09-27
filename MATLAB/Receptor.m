iteraciones = 1;

connectedRadios = findsdru; %busca si hay USRP conectados
platform = connectedRadios(1).Platform; 


num_mediciones = input("¿Cuantas medidas va a realizar?");


centerFreq = input("¿Que frecuencia desea sintonizar en MHz?\n");


radioMasterClockRate = 2e7; %frecuencia de muestreo del radio
radioGain = 30; %ganancia del radio
radioDecimationFactor = 100; %factor de decimacion del radio
radioFrameLength = 4e3; %longitud de la trama, muestras/trama

Fs = radioMasterClockRate/radioDecimationFactor; %frecuencia de muestreo en banda base para el computador, muestras/segundo

frameTime = 1/(Fs/radioFrameLength); %duracion de la trama en segundos, segundos/trama

stopTime = 2; %valor en segundos del tiempo total de muestreo


question1 = input("0 -> realizar el analisis para una trama \n 1-> realizar el analisis para todas las tramas recolectadas en un segundo \n");

if question1
    signals = []; %vector donde se almacenan las senales completas
    signals1 = []; %vector donde se almaceran las tramas
else
    signals = [];
end


while true
    
    in = input("Presione enter para continuar."); %no se debe presionar enter hasta no haber calibrado
    
    
    %CONFIGURACION DEL RADIO
    radio = comm.SDRuReceiver(...
          'Platform', 'B210', ...
          'SerialNum', '30F40F4', ...
          'MasterClockRate', radioMasterClockRate);


    %SerialNum debe ser el serial del USRP

    radio.CenterFrequency  = centerFreq*(10^6);
    radio.Gain = radioGain;
    radio.DecimationFactor = radioDecimationFactor;
    radio.SamplesPerFrame = radioFrameLength;
    radio.OutputDataType = 'single';

    
    %TOMA DE MUESTRAS
    for index = iteraciones: num_mediciones
        

            signal = 0;
            len = 0;

            question = input(index+"° medida a realizar.\n 0 -> Realizar medida.\n 1 -> Calibrar.\n");
            
            if question 
                break
            end
            
            timeCounter = 0;
            while timeCounter < stopTime
                [signal, len] = step(radio);
                if len > 0 %len es el numero de muestras provistas desde el USRP.
                  % Update counter
                  timeCounter = timeCounter + frameTime; %se actualiza el contador despues de obtenida la trama,
                                                        %el tiempo que transcurre esta dado por la duracion de la trama.                                                     

                   if question1 && (timeCounter <= 1 + frameTime) %almacenar todas las muestras en 1 segundo
                      signals1 = [signals1; signal];%se empieza a llenar con tramas al vector, correspondiente a una sola medida
                   end
                
                end
            end
            
            if question1 %para todas las tramas en 1 segundo
                
                signals = [signals, signals1]; %se concatena cada medida de 1 segundo
            else
                signals = [signals, signal]; %se concatena cada medida indicado por la duracion de la trama
            end
            signals1 = [];


    end
    
    release(radio) %se libera al radio
    iteraciones = index;
    
    if index == num_mediciones %iteraciones completadas
        break
    end
    


end


%GUARDAR LAS SENALES EN UN ARCHIVO
fechadoc = datestr(datetime('now')); 
fechadoc = strrep(fechadoc,'-','_');
fechadoc = strrep(fechadoc,' ','_');
fechadoc = strrep(fechadoc,':','_');
namedoc = strcat(fechadoc,'signals','.mat');
save(namedoc,'signals')

questionFilter = input("0 -> Obtener solo la portadora. \n 1 -> Obtener el tono.");
power = zeros(1, num_mediciones); %Vector que almacena la potencia promedio de cada medida
%el tono es de 50KHz
if questionFilter
        %FILTROS
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
    %FILTRADO Y OBTENCION DE POTENCIA DE CADA MEDIDA
        for index2 = 1:num_mediciones

            filteredsignalhp = FIRHPF(signals(:,index2));
            filteredsignallp = FIRLPF(filteredsignalhp);
            signalrms = rms(filteredsignallp);
            power(index2) = signalrms^2;

        end
    
else
    
     filtertype = 'FIR';
     Fpass = 4e3;
     Fstop = 8e3; 
     Rp = 0.1;
     Astop = 80;
     FIRLPF = dsp.LowpassFilter('SampleRate',Fs, ...
                                'FilterType',filtertype, ...
                                'PassbandFrequency',Fpass, ...
                                'StopbandFrequency',Fstop, ...
                                'PassbandRipple',Rp, ...
                                'StopbandAttenuation',Astop);
                            
     

    %FILTRADO Y OBTENCION DE POTENCIA DE CADA MEDIDA
     for index2 = 1:num_mediciones
        filteredsignallp = FIRLPF(signals(:,index2));
        signalrms = rms(filteredsignallp);
        power(index2) = signalrms^2;

     end
                            
                            
end


%NORMALIZACION DE POTENCIA
power(1) = power(length(power));
powerNormalized = power/max(power);

%NOMBRE PARA GUARDAR LAS FIGURAS
fechadoc1 = datestr(datetime('now'));
fechadoc1 = strrep(fechadoc1,'-','_');
fechadoc1 = strrep(fechadoc1,' ','_');
fechadoc1 = strrep(fechadoc1,':','_');
namedoc1 = strcat(fechadoc1,'pattern.fig');



angles = 0:2*pi/(num_mediciones-1):2*pi; %vector de angulos
   
%GRAFICA
figure
polarplot(angles, powerNormalized)
savefig(namedoc1)

