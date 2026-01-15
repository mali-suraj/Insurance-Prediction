# Logistic Regression Model

A machine learning project implementing logistic regression for insurance data classification.

## Project Structure

- `app.py` - Flask web application
- `train_model.py` - Model training script
- `insurance_data.csv` - Dataset for training
- `models/` - Trained model storage
- `templates/` - HTML templates for the web interface
- `requirements.txt` - Python dependencies

## Installation

1. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

### Training the Model
```bash
python train_model.py
```

### Running the Web Application
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Features

- Logistic regression classification model
- Web-based user interface
- Real-time predictions on insurance data

## Dataset

The `insurance_data.csv` file contains the training dataset used for the logistic regression model.

## License

This project is open source and available under the MIT License.
