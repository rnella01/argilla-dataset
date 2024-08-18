import argilla as rg

from datasets import load_dataset, Dataset
# from setfit import SetFitModel, Trainer, get_templated_dataset, sample_dataset


client = rg.Argilla(
    api_url="https://rnella01-my-argilla.hf.space",
    api_key="lDVrtbheYJ5WKvqJ8TBeg3aJw_wVjJgQpppZlTf4hdjx3NeiSj-Fs_X16A37w_7EVgFIzJ45zeuUwdkS_7xy4xsVy_PrBXAfVlgs6WSfVCY"
)


labels = ["sdoh_positive", "sdoh_negative"]

settings = rg.Settings(
    guidelines="Classify the reviews as sdoh_positive or negative.",
    fields=[
        rg.TextField(
            name="text",
            title="Text extracted from SDOH doc",
            use_markdown=False,
        ),
    ],
    questions=[
        rg.LabelQuestion(
            name="my_label",
            title="Is this an SDOH doc?",
            labels=labels,
        )
    ],
)

dataset = rg.Dataset(
    name="sdoh_classification_dataset",
    settings=settings,
    client=client,
    workspace="argilla"
)
dataset.create()

records = [
    rg.Record(
        fields={
            "text": "low income.",
        },
    ),
    rg.Record(
        fields={
            "text": "unhealthy due to lack of access to healthy food.",
        },
    ),
    rg.Record(
        fields={
            "text": "healthy due to access to healthy food.",
        },
    ),
]
dataset.records.log(records)
