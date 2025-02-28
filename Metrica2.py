% Configuración del canal de ThingSpeak
channelID = 2857074;  
readAPIKey = 'H9CG3ENUZ2AZOGVG';  
writeAPIKey = 'MI68CW04GSQP2VN7';  

% Número de mediciones a promediar
numSamples = 10;  

% Intentar leer los últimos 10 datos del canal
try
    data = thingSpeakRead(channelID, 'NumPoints', numSamples, 'ReadKey', readAPIKey);
catch e
    fprintf("⚠️ Error al leer datos de ThingSpeak: %s\n", e.message);
    return;
end

% Verificar si se obtuvieron datos correctamente
if isempty(data)
    fprintf("⚠️ No se pudieron leer los datos de ThingSpeak.\n");
else
    % Verificar si hay suficientes datos y que no sean NaN
    data = data(~isnan(data));  % Eliminar valores NaN antes de calcular el promedio
    
    if length(data) < numSamples
        fprintf("⚠️ Advertencia: Hay menos de 10 datos disponibles en el canal.\n");
    end
    
    % Calcular el promedio de temperatura
    avgTemp = mean(data);

    % Verificar si el promedio es un número válido antes de escribirlo
    if isnan(avgTemp)
        fprintf("⚠️ Error: El promedio de temperatura es NaN. No se enviará a ThingSpeak.\n");
    else
        % Mostrar el resultado en consola
        fprintf("✅ Promedio de temperatura de las últimas %d mediciones: %.2f°C\n", length(data), avgTemp);

        % Guardar el promedio en ThingSpeak en Field 2
        try
            thingSpeakWrite(channelID, avgTemp, 'WriteKey', writeAPIKey, 'Fields', 2);
            fprintf("✅ Promedio de temperatura guardado en ThingSpeak (Field 2).\n");
        catch e
            fprintf("⚠️ Error al escribir en ThingSpeak: %s\n", e.message);
        end
    end
end
