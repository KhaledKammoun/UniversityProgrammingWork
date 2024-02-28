from mrjob.job import MRJob
class MRWordFrequencyCount(MRJob) :
    def mapper(self,_,line) :
        words = line.split()
        for word in words :
            yield word.lower(), 1
        
    def reducer(self, key, values) :
        yield key, sum(values)

    def max_film(self, key, values) :
        max_val = 0
        for value in values :
            max_val = max(max_val, value)
        
if __name__ == '__main__' :
    MRWordFrequencyCount.run()
    