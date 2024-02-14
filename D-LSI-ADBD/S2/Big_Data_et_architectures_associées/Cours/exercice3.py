from mrjob.job import MRJob
class MRWordFrequencyCount(MRJob) :
    def mapper(self,_,line) :
        line_split = line.split(',')

        if line_split[2].upper() == "TMAX" :
            temperature = line_split[3]
            yield line_split[0], temperature
            
    def reducer(self, location, temps) :
        yield location, max(temps)
if __name__ == '__main__' :
    MRWordFrequencyCount.run()

