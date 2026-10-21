"use client";

import React, { useState } from "react";
import { motion } from "framer-motion";
import TableOfContents from "@/app/components/TableOfContents";
import NavigateButton from "@/app/components/NavigateButton";

export default function page() {
  const [tableOpen, setTableOpen] = useState(false);
  const contents = [
    {
      title: "Theory Questions",
      href: "#theory",
    },
    {
      title: "Problem-Solving Process",
      href: "#process",
    },
    {
      title:
        "Practice Example: Titanic: Binary Classification – Predict Survival",
      href: "#practice-titanic",
    },
  ];

  return (
    <div className="flex flex-col min-h-full h-fit w-full gap-3">
      <motion.section
        initial={{ y: -100, opacity: 0 }}
        animate={{ y: 0, opacity: 1 }}
        transition={{ duration: 0.3, ease: "easeOut" }}
        className="h-fit bg-white w-full
        flex flex-col justify-center items-center p-4 lg:px-[10%]
        text-black text-center border-b-2"
      >
        <h2 className="text-[40px] font-bold">
          Lesson 2: Begginer to Artificial Intelligence -
          Machine Learning - Deep Learning & Problem-Solving
          Progcess
        </h2>

        <p className="text-[25px]">
          Source:{" "}
          <a
            href="https://codedream.edu.vn/"
            className="underline"
          >
            Code Dream
          </a>
          ,{" "}
          <a
            href="https://www.kaggle.com/"
            className="underline"
          >
            Kaggle
          </a>
          ,{" "}
          <a
            href="https://chatgpt.com/"
            className="underline"
          >
            ChatGPT
          </a>
        </p>
      </motion.section>

      <div className="w-full lg:w-[80%] px-4 mx-auto">
        <NavigateButton lesson={2} />

        <TableOfContents data={contents} />

        <motion.div
          initial={{ x: 200, opacity: 0 }}
          animate={{ x: 0, opacity: 1 }}
          className="p-3 flex-col gap-3 mt-5"
          id="theory"
        >
          <h3 className="text-[30px] font-semibold">
            Theory Questions
          </h3>

          <p className="text-[25px] ps-3">
            <b>1. Main difference between ML and DL?</b>
            <br />
            Ans: DL is a branch of ML that uses deep neural
            networks to learn complex representations
            automatically. ML can learn rules from data but
            may not extract high-level features like DL. DL
            usually requires more data and compute. <br />
            <b>2. Why can a model be biased? Example</b>
            <br />
            Ans: A model can be biased if the training data
            is imbalanced or not representative. Example: If
            class A makes up 90% of the data and class B
            10%, the model may predict A more often and
            perform poorly on B. <br />
            <b>
              3. Which approach to start with for these
              problems? Rule-based or ML or DL?
            </b>
            <br />
            a. Forecast customers cancel service (CRM data
            table). <br />
            Ans: ML.
            <br />
            b. Recognition Traffic Sign from image. <br />
            Ans: DL.
            <br />
            c. Autofill forms by fixed rules. <br />
            Ans: Rule-based.
            <br />
            <b>
              4. Why still require a validation set even if
              we have a test set?
            </b>
            <br />
            Ans: Validation is used to tune hyperparameters
            and select the best model without looking at the
            test set. The test set is only used for final
            evaluation to measure real performance on unseen
            data. <br />
            <b> 5. Which is data leakage? </b> <br />
            a. Fit StandardScaler on train then transform
            test. <br />
            b. Use median/mean calculated from the whole
            dataset to impute train/val/test <br />
            Ans: Leakage is information of test or future
            has leaked into training progress. So, b is
            leakage because information from the
            test/validation data is used during training.
            <br />
            <b>
              6. For imbalanced classification, which
              metrics are better than Accuracy? Precision or
              Recall or F1 or ROC-AUC?
            </b>
            <br />
            Ans: <br />
            - Precision: % of predicted positives that are
            correct. <br />
            - Recall: % of actual positives that are
            correctly predicted. <br />- F1-score: Harmonic
            mean of Precision and Recall. <br /> - ROC-AUC:
            Measures the model’s ability to distinguish
            classes across thresholds. <br />
            - Summary: F1-score and ROC-AUC are usually
            preferred for imbalanced datasets.. <br />
            <b>
              7. Purpose of a baseline in a pipeline?
            </b>{" "}
            <br />
            Ans: <br />- Provides a minimum reference
            performance to check if the model learns
            anything useful. <br />
            - Validates that data loading and preprocessing
            work correctly. <br />- Helps set expectations
            for model improvement. <br />
            <b>
              8. When shouldn’t you merge train and
              validation for final training?
            </b>
            <br />
            Ans: <br />
            - When you still need validation for
            hyperparameter tuning. <br />- When data is
            limited and you want an independent set to
            evaluate generalization. <br />- For deep
            learning with early stopping, validation is
            needed to stop training correctly. <br />- For
            time-series data, merging may leak future
            information.
          </p>

          <p></p>
        </motion.div>

        <motion.div
          initial={{ x: -100, opacity: 0 }}
          animate={{ x: 0, opacity: 1 }}
          className="p-3 flex-col gap-3 mt-3"
          id="process"
        >
          <h3 className="text-[30px] font-semibold">
            Problem-Solving Process
          </h3>

          {/* 1. Define the Goals */}
          <h6 className="text-[27px] underline mt-2">
            1. Define the Goals
          </h6>
          <p className="text-[25px] ps-3">
            <b>Type of Problems:</b> <br />-{" "}
            <b>Regression:</b> Predict real-valued numbers
            (e.g., house prices, temperature). <br />-{" "}
            <b>Classification:</b> Predict discrete labels
            (e.g., spam / not spam, survived / not
            survived). <br />- <b>Unsupervised:</b> Discover
            patterns or structures without labels (e.g.,
            Clustering, PCA). <br />
            <br />
            <b>Main Evaluation Metrics:</b> <br />-{" "}
            <b>Regression:</b> MAE, RMSE, R². <br />-{" "}
            <b>Classification:</b> Accuracy,
            Precision/Recall/F1, ROC-AUC. <br />-{" "}
            <b>Clustering:</b> Silhouette Score. <br />-{" "}
            <b>Dimensionality Reduction:</b> Visualization
            or downstream task. <br />
            <br />
            <b>Real-world Constraints:</b> <br />
            - Allowed inference time (ms/seconds). <br />-
            Acceptable error margin / accuracy threshold.{" "}
            <br />
            - Available resources (CPU/GPU/memory), cost,
            explainability. <br />
            - Risk of Type I/II errors (e.g., missing cancer
            vs false alarms). <br />
            <br />
            <b>Example Goal:</b> <br />
            “Build a spam email classification model with F1
            ≥ 0.92, inference latency &lt; 50ms/email,
            prioritize Recall to minimize missed spam.”
          </p>

          {/* 2. Data Collection & Exploration */}
          <h6 className="text-[27px] underline mt-2">
            2. Data Collection & Exploration (EDA)
          </h6>
          <p className="text-[25px] ps-3">
            <b>Goal:</b> Understand the dataset and detect
            data issues. <br />
            <br />
            <b>Quick Overview:</b> <br />
            <code>
              df.shape <br />
              df.columns <br />
              df.dtypes <br />
              df.info() <br />
              df.describe()
            </code>{" "}
            <br />
            <br />
            <b>Check for:</b> <br />- Number of numerical vs
            categorical features. <br />
            - Missing values (%). <br />
            - Outliers or extreme values. <br />
            - Class imbalance (for classification). <br />
            - Redundant or irrelevant columns. <br />
          </p>

          {/* 3. Data Splitting */}
          <h6 className="text-[27px] underline mt-2">
            3. Data Splitting
          </h6>
          <p className="text-[25px] ps-3">
            <b>Golden Rule:</b> Split dataset <b>before</b>{" "}
            any preprocessing to avoid data leakage. <br />
            - Train: learn model parameters. <br />
            - Validation: tune hyperparameters. <br />
            - Test: final evaluation; only open once. <br />
            <br />
            <b>Methods:</b> <br />
            - Random split (e.g., 70/15/15), stratify if
            classification. <br />
            - Time series split: past → train, future →
            val/test. <br />
            - Group split: avoid same group in train &
            val/test. <br />- K-Fold CV: rotate folds for
            robust estimates.
          </p>

          {/* 4. Data Preprocessing */}
          <h6 className="text-[27px] underline mt-2">
            4. Data Preprocessing
          </h6>
          <p className="text-[25px] ps-3">
            <b>Goal:</b> Clean, consistent, model-ready
            data. <br />
            <br />
            <b>Important:</b> Fit all transformations on{" "}
            <b>train only</b> and apply to val/test. <br />-{" "}
            <b>Missing Values:</b> Numeric: median/mean;
            Categorical: most frequent/"Unknown"; Optional:
            KNNImputer. <br />- <b>Encoding:</b> One-Hot for
            categorical (no order), Ordinal for ordered
            features, merge rare levels. <br />-{" "}
            <b>Scaling:</b> StandardScaler for
            regression/logistic/SVM/KNN; Tree models usually
            do not require scaling. <br />- <b>Outliers:</b>{" "}
            Clip/winsorize for linear models; trees less
            sensitive. <br />- <b>Feature Engineering:</b>{" "}
            Combine features (e.g., FamilySize = SibSp +
            Parch + 1), extract date/time components,
            cluster lat/long. Fit new features only on
            train.
          </p>

          {/* 5. Model Selection */}
          <h6 className="text-[27px] underline mt-2">
            5. Model Selection
          </h6>
          <p className="text-[25px] ps-3">
            <b>Baseline:</b> DummyRegressor/Classifier.{" "}
            <br />
            <b>Basic Models:</b> Linear Regression,
            Ridge/Lasso, Logistic Regression, KNN, Decision
            Tree. <br />
            <b>Advanced Models:</b> Random Forest, Gradient
            Boosting (XGBoost/LightGBM/CatBoost), SVM, Deep
            Learning (MLP/CNN/RNN/Transformer). <br />
            Choose 2–3 models and compare fairly.
          </p>

          {/* 6. Training & Validation */}
          <h6 className="text-[27px] underline mt-2">
            6. Training & Validation
          </h6>
          <p className="text-[25px] ps-3">
            - Train model on <b>train set</b>. <br />- Tune
            hyperparameters using <b>validation set</b> or
            K-Fold CV. <br />
            - Use GridSearchCV / RandomizedSearchCV / Early
            stopping. <br />- Wrap preprocessing + model in
            Pipeline/ColumnTransformer to prevent leakage.{" "}
            <br />- Fix random_state for reproducibility.
          </p>

          {/* 7. Model Evaluation */}
          <h6 className="text-[27px] underline mt-2">
            7. Model Evaluation
          </h6>
          <p className="text-[25px] ps-3">
            <b>Regression:</b> MAE, RMSE, R²; residual
            plots. <br />
            <b>Classification:</b> Precision, Recall, F1,
            ROC-AUC; confusion matrix. <br />- Evaluate only
            on <b>test set</b>, keep untouched until final
            evaluation. <br />
            <br />
            <b>Prevent Data Leakage:</b> <br />
            - Fit transformers only on train. <br />- Avoid
            target leakage & temporal leakage. <br />- Use
            GroupKFold / GroupShuffleSplit if needed. <br />
            - Never peek at test multiple times.
          </p>
        </motion.div>

        <motion.div
          initial={{ x: 200, opacity: 0 }}
          animate={{ x: 0, opacity: 1 }}
          className="p-3 flex-col gap-3 mt-3"
          id="practice-titanic"
        >
          <h3 className="text-[30px] font-semibold">
            Practice Example: Titanic: Binary Classification
            – Predict Survival
          </h3>

          <h6 className="text-[27px] mt-2">
            Dataset:{" "}
            <a
              href="https://www.kaggle.com/c/titanic"
              className="underline"
            >
              Titanic - Machine Learning from Disaster
            </a>
          </h6>

          <h6 className="text-[27px] underline mt-2">
            1. Define the Goals:
          </h6>
          <p className="text-[25px] ps-3">
            - Type of Problem: Classification. <br />- Main
            Evaluation Metrics: Accuracy,
            Precision/Recall/F1, ROC-AUC. <br />
          </p>
        </motion.div>

        <NavigateButton lesson={2} />
      </div>
    </div>
  );
}
