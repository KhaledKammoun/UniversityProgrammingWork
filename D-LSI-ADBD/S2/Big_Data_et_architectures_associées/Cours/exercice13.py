from mrjob.job import MRJob
from mrjob.step import MRStep

class MRWordFrequencyCount(MRJob) :
    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer),
            MRStep(reducer=self.reducer_find_max)
        ]

    def mapper(self,_,line) :
        words = line.split()
        
        [_, movie, _, _] = words[:4]
        yield movie, 1
    def reducer(self, key, values) :
        total_count = sum(values)
        yield None, (total_count, key)

    def reducer_find_max(self, _, movie_counts):
        yield max(movie_counts)
    
if __name__ == '__main__' :
    MRWordFrequencyCount.run()


