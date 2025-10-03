# Speech Sentiment Recognition

A compact research/prototype project that extracts audio features from speech and trains models to predict emotional sentiment.

This repo contains scripts and notebooks for dataset download, feature extraction (librosa), model training (classical ML and CNN), and evaluation. The most complete workflows are in `notebooks/`.

Tech stack

- Python 3.10+
- numpy, pandas
- librosa (audio feature extraction)
- scikit-learn (random forest, metrics)
- tensorflow / keras (CNN experiments)
- matplotlib, seaborn (plots)
- kaggle (optional, dataset downloader)

Key graphics

Confusion matrix (model evaluation):

![Confusion Matrix](graphics/confusion_matrix.jpg "Confusion matrix")

Feature importance (random forest):

![Feature Importance](graphics/feature_importance.jpg "Feature importance")

RMS energy distribution:

![RMS energy distribution](graphics/rms_energy_plot.png "RMS energy distribution across emotions")

MFCCs variance distribution:

![MFCCs variance distribution](graphics/mfccs_variance_plot.png "MFCCs variance across emotions")

Tonnetz variance distribution:

![Tonnetz variance distribution](graphics/tonnetz_variance_plot.png "Tonnetz variance across emotions")

Quick pointers

- See `notebooks/ESRmodels.ipynb` for the extraction → training → evaluation pipeline.
- Use `scripts/dataset_downloader.py` to fetch datasets (requires Kaggle CLI and `kaggle.json`).
- Install dependencies with `pip install -r requirements.txt`.