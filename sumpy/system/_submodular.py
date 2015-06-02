from sumpy.system._base import _SystemBase
from sumpy.annotators import SubmodularMMRMixin
from sumpy.document import Summary

class SubmodularMMRSummarizer(SubmodularMMRMixin, _SystemBase):
    def __init__(self, sentence_tokenizer=None, word_tokenizer=None,
            lam=.3, budget_type="word", budget_size=400, scale=.2,
            verbose=False):
        self.sentence_tokenizer = sentence_tokenizer
        self.word_tokenizer = word_tokenizer
        self.lam = lam
        self.scale = scale
        self.budget_type = budget_type
        self.budget_size = budget_size

        super(SubmodularMMRSummarizer, self).__init__(verbose=verbose)

    def build_summary(self, input_df, ndarray_data):
        output_df = input_df[input_df["f:submodular-mmr"].isnull() == False]
        output_df = output_df.sort(["doc id", "sent id"], ascending=True)
        print output_df
        print output_df['sent text'].apply(len)
        return Summary(output_df)
