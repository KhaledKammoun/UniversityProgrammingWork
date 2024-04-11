from mrjob.job import MRJob
from mrjob.step import MRStep

class SpendByCustomer(MRJob) :

    def mapper(self, _, line) :
        words = line.split(',')
        yield words[0], float(words[2])

    def reducer(self, key, values) :
        yield key, sum(values)

    def converter(self, key, values) :
        for value in values :
            yield key, float(value) / 3.6
    
    def steps(self) :
        return [
            MRStep(mapper=self.mapper, reducer=self.converter),
            MRStep(reducer=self.reducer)
        ]
if __name__ == '__main__' :
    SpendByCustomer.run()