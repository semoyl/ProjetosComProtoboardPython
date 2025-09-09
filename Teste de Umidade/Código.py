from machine import Pin, ADC
import time

PINO_SENSOR_UMIDADE = 34

PINO_LED_SECO = 26

sensor_umidade = ADC(Pin(PINO_SENSOR_UMIDADE))

led_seco = Pin(PINO_LED_SECO, Pin.OUT)

sensor_umidade.width(ADC.WIDTH_12BIT)

sensor_umidade.atten(ADC.ATB_11DB)

while True:
    valor_umidade = sensor_umidade.read()
    
    print("Valor do sensor:", valor_umidade)
    
    
    LIMIAR_SECO = 2000
    
    if valor_umidade > LIMIAR_SECO:
            print("ALERTA: Solo seco! É hora de regar.")
            led_seco.value(1)
    else:
        print("Solo Úmido. Tudo Certo!")
        led_seco.value(0)
        
    time.sleep(5)