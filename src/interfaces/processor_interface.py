# Интерфейс для процессоров
import pandas as pd
from joblib import Parallel, delayed


class ProcessorInterface:
    """Метод, реализующие интерфейс для процессора (выделение фич, препроцессинг...)"""

    def __init__(self) -> None:
        pass

    def feature_construct(self, df: pd.DataFrame, column_name: str = "trn_purp", is_cuda: bool = False) -> pd.DataFrame:
        """Метод для выделения фич"""
        return df

    def multi_feature_construct(
        self, df: pd.DataFrame, column_name: str, chunk_size: int = 5000, n_cores: int = 8, is_cuda: bool = False
    ) -> pd.DataFrame:
        """Метод для параллельного выделения фич"""
        dfs = [df[i : i + chunk_size] for i in range(0, len(df), chunk_size)]
        results = Parallel(n_jobs=n_cores)(delayed(self.feature_construct)(X, column_name, is_cuda) for X in dfs)

        # Если получился словарь (для эмбеддингов):
        if isinstance(results[0], dict):
            data = {}
            for d in results:
                data.update(d)
        # Если получился датафрейм (для остального):
        elif isinstance(results[0], (pd.DataFrame, pd.Series)):
            data = pd.concat(results)
        return data

    def transform(
        self,
        df: pd.DataFrame,
        column_name: str = "trn_purp",
        chunk_size: int = 500,
        n_jobs: int = 1,
        n_cores: int = 8,
        is_cuda: bool = False,
    ) -> pd.DataFrame:
        """Метод для преобразования входящего df с возможностью выбора синхронного или параллельного режима"""
        if n_jobs == 1:
            df = self.feature_construct(df, column_name, is_cuda=is_cuda)
        elif n_jobs == -1:
            df = self.multi_feature_construct(df, column_name, chunk_size=chunk_size, n_cores=n_cores, is_cuda=is_cuda)

        return df
