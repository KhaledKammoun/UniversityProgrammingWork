from mrjob.job import MRJob
class MRWordFrequencyCount(MRJob) :
    def MakeFahrenheit(self, tenthsOfCelsius) :
        celsius = float(tenthsOfCelsius) / 10.0
        fahrenheit = celsius * 1.8 + 32.0
        return fahrenheit

    def mapper(self,_,line) :
        line_split = line.split(',')

        if line_split[2] == "TMAX" :
            temperature = self.MakeFahrenheit(line_split[1]) #data = line_split[1]
            yield line_split[0], temperature
            
    def reducer(self, location, temps) :
        yield location, max(temps)
if __name__ == '__main__' :
    MRWordFrequencyCount.run()

