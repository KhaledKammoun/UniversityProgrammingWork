from mrjob.job import MRJob
from mrjob.step import MRStep

class SpendByCustomer(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_words, reducer=self.reducer_count_words),
            MRStep(mapper=self.mapper_make_counts_key, reducer=self.reducer_output_words)
        ]

    def mapper_get_words(self, _, line): 
        customerID, _, orderAmount = line.split(',')
        yield customerID, float(orderAmount)

    def reducer_count_words(self, customerID, orderAmounts):
        yield customerID, sum(orderAmounts)

    def mapper_make_counts_key(self, customerID, orderAmount):
        yield '%04.02f' % float(orderAmount), customerID

    def reducer_output_words(self, orderAmount, customerIDs):
        for customerID in customerIDs:
            yield customerID, orderAmount

if __name__ == '__main__':
    SpendByCustomer.run()
