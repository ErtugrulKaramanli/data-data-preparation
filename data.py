import os
import pandas as pd
from pathlib import Path

class Olist:
    def __init__(self):
        # CSV klasörünün yolunu tanımla
        self.csv_path = Path(os.path.expanduser("~/.workintech/olist/data/csv"))

    def ping(self):
        """Kurulum kontrolü için pong döndürür."""
        return "pong"

    def get_data(self):
        """
        Klasördeki tüm CSV dosyalarını okur, temiz isimlerle
        bir veri sözlüğü (dictionary) döndürür.
        """
        file_paths = list(self.csv_path.iterdir())
        
        file_names = [path.name for path in file_paths if path.suffix == '.csv']
        
        key_names = [
            name.replace('olist_', '').replace('_dataset.csv', '').replace('.csv', '') 
            for name in file_names
        ]
        
        data = {key: pd.read_csv(path) for key, path in zip(key_names, file_paths)}
        
        return data
