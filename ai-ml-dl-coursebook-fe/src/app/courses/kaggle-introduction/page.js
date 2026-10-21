"use client";

import React, { useState } from "react";
import { motion } from "framer-motion";
import TableOfContents from "@/app/components/TableOfContents";
import NavigateButton from "@/app/components/NavigateButton";

export default function page() {
  const [tableOpen, setTableOpen] = useState(false);
  const contents = [
    {
      title: "1. About Kaggle",
      href: "#about",
    },
    {
      title:
        "2. Use Kaggle to practice Data Science skills",
      href: "#data-science",
    },
    {
      title: "3. Use Kaggle to study and practice AI/ML/DL",
      href: "#ai-ml-dl",
    },
  ];

  const ai_ml_dl_courses = [
    {
      title: "Intro to Machine Learning",
      href: "https://www.kaggle.com/learn/intro-to-machine-learning",
    },
    {
      title: "Intermediate Machine Learning",
      href: "https://www.kaggle.com/learn/intermediate-machine-learning",
    },
    {
      title: "Feature Engineering",
      href: "https://www.kaggle.com/learn/feature-engineering",
    },
    {
      title: "Machine Learning Explainability",
      href: "https://www.kaggle.com/learn/machine-learning-explainability",
    },
    {
      title: "Intro to Deep Learning",
      href: "https://www.kaggle.com/learn/intro-to-deep-learning",
    },
    {
      title: "Computer Vision",
      href: "https://www.kaggle.com/learn/computer-vision",
    },
    {
      title: "Time Series",
      href: "https://www.kaggle.com/learn/time-series",
    },
    {
      title: "Intro to Game AI and Reinforcement Learning",
      href: "https://www.kaggle.com/learn/intro-to-game-ai-and-reinforcement-learning",
    },
    {
      title: "Intro to AI Ethics",
      href: "https://www.kaggle.com/learn/intro-to-ai-ethics",
    },
  ];

  const data_science_courses = [
    {
      title: "Intro to Programming",
      href: "https://www.kaggle.com/learn/intro-to-programming",
    },
    {
      title: "Data Cleaning",
      href: "https://www.kaggle.com/learn/data-cleaning",
    },
    {
      title: "Data Visualization",
      href: "https://www.kaggle.com/learn/data-visualization",
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
          Introduction of Kaggle
        </h2>
      </motion.section>

      <div className="w-full lg:w-[80%] px-4 mx-auto">
        <NavigateButton lesson={2} />

        <TableOfContents
          data={contents}
          tableOpen={tableOpen}
          setTableOpen={setTableOpen}
        />

        <motion.div
          initial={{ x: 200, opacity: 0 }}
          animate={{ x: 0, opacity: 1 }}
          className="p-3 flex-col gap-3 mt-5"
          id="about"
        >
          <h3 className="text-[30px] font-semibold">
            1. About Kaggle
          </h3>
          <p className="text-[25px]">
            Kaggle is an online platform owned by Google
            that serves as a community for data scientists,
            machine learning engineers, and AI enthusiasts.
            It’s one of the best places to learn, practice,
            and showcase your skills in data analysis and
            machine learning.
          </p>
        </motion.div>

        <motion.div
          initial={{ x: -100, opacity: 0 }}
          animate={{ x: 0, opacity: 1 }}
          className="p-3 flex-col gap-3 mt-3"
          id="data-science"
        >
          <h3 className="text-[30px] font-semibold">
            2. Use Kaggle to practice Data Science skills
          </h3>
          <div className="flex flex-col p-2 gap-2 text-[25px]">
            {data_science_courses.map(
              ({ title, href }, index) => (
                <a
                  href={href}
                  key={href}
                  className="underline"
                >
                  {index + 1}. {title}
                </a>
              )
            )}
          </div>
        </motion.div>

        <motion.div
          initial={{ x: 200, opacity: 0 }}
          animate={{ x: 0, opacity: 1 }}
          className="p-3 flex-col gap-3 mt-3"
          id="ai-ml-dl"
        >
          <h3 className="text-[30px] font-semibold">
            3. Use Kaggle to study and practice AI/ML/DL
          </h3>
          <div className="flex flex-col p-2 gap-2 text-[25px]">
            {ai_ml_dl_courses.map(
              ({ title, href }, index) => (
                <a
                  href={href}
                  key={href}
                  className="underline"
                >
                  {index + 1}. {title}
                </a>
              )
            )}
          </div>
        </motion.div>

        <NavigateButton lesson={2} />
      </div>
    </div>
  );
}
