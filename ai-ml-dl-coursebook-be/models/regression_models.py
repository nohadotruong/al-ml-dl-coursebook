from sklearn.pipeline import Pipeline
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.model_selection import GridSearchCV


def train_dummy_model(preprocess, X_train, y_train, X_val, X_test, strategy="mean"):
    model = Pipeline([("prep", preprocess), ("reg", DummyRegressor(strategy=strategy))])
    model.fit(X_train, y_train)
    return {
        "model": model,
        "y_pred_val": model.predict(X_val),
        "y_pred_test": model.predict(X_test),
    }


def train_linear_model(preprocess, X_train, y_train, X_val, X_test):
    model = Pipeline([("prep", preprocess), ("reg", LinearRegression())])
    model.fit(X_train, y_train)
    return {
        "model": model,
        "y_pred_val": model.predict(X_val),
        "y_pred_test": model.predict(X_test),
    }


def train_ridge_model(
    preprocess, X_train, y_train, X_val, X_test, alphas=[0.1, 1, 10, 100]
):
    pipe = Pipeline([("prep", preprocess), ("reg", Ridge())])
    param_grid = {"reg__alpha": [0.1, 1.0, 10.0, 100.0]}
    grid = GridSearchCV(pipe, param_grid, cv=5, scoring="neg_mean_absolute_error")
    grid.fit(X_train, y_train)
    best_model = grid.best_estimator_
    return {
        "model": best_model,
        "best_alpha": grid.best_params_["reg__alpha"],
        "y_pred_val": best_model.predict(X_val),
        "y_pred_test": best_model.predict(X_test),
    }
