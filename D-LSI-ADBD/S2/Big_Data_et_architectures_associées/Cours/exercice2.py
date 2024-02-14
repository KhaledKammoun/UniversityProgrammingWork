from mrjob.job import MRJob
class MRWordFrequencyCount(MRJob) :
    def mapper(self,_,line) :
        rating = line.split()[2]
        yield rating.lower(), 1
    def reducer(self, rating, occurences) :
        yield rating, sum(occurences)
if __name__ == '__main__' :
    MRWordFrequencyCount.run()
