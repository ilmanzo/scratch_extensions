#!/usr/bin/python
#estensione sperimentale per l'ambiente Scratch Offline 2.0
#per usarla: 
# - eseguire questo script
# - collegarsi con un browser a http://localhost:4000
# - scaricare il file .json proposto dal primo link
# - aprire scratch e fare click sul menu "File" tenendo premuto il tasto shift
# - importare il file json scaricato prima (contiene la definizione dell'estensione)
# - tenere in esecuzione questo script
# - dentro Scratch appariranno due nuove variabili

#TODO: semplificare il deploy

import blockext
import yweather

class MeteoExtension:
    def __init__(self):
        client = yweather.Client()
        woeid=client.fetch_woeid("Verona, Italy")
        self.weather=client.fetch_weather(woeid,metric=True)
        
    def get_massima(self):
        return self.weather["forecast"][1]["high"]
    
    def get_minima(self):
        return self.weather["forecast"][1]["low"]
    
        
descriptor=blockext.Descriptor(
    name="MeteoScratch",
    port=4000,
    blocks=[
        blockext.Block('get_minima','reporter','temp minima domani'),
        blockext.Block('get_massima','reporter','temp massima domani'),
    ]
)

extension=blockext.Extension(MeteoExtension,descriptor)

if __name__=="__main__":
    extension.run_forever(debug=True)
