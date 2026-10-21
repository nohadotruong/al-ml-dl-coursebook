import { BookA, House, MonitorDown } from "lucide-react";

export const menu = [
  {
    label: "Home",
    href: "/",
    icon: <House className="min-w-9 min-h-9" />,
  },
  {
    label: "Setup",
    href: "/setup",
    icon: <MonitorDown className="min-w-9 min-h-9" />,
  },
  {
    label: "Course",
    href: "/courses",
    icon: <BookA className="min-w-9 min-h-9" />,
  },
];

export const homeMenu = [
  {
    title: "Environment Setup",
    href: "/setup",
    subMenu: [
      {
        label: "Python",
        href: "/setup/python",
      },
      {
        label: "Visual Studio Code",
        href: "/setup/vscode",
      },
    ],
  },
  {
    title: "Courses",
    href: "/courses",
    subMenu: [
      {
        label:
          "Begginer to AI/ML/DL and Problem-Solving Process",
        href: "/courses/lesson1",
      },
      {
        label: "Linear Regression and Optimization",
        href: "/courses/lesson1",
      },
      {
        label: "Classification Problem and Evaluation",
        href: "/courses/lesson1",
      },
      {
        label: "Clustering and Dimensionality Reduction",
        href: "/courses/lesson1",
      },
      {
        label: "Basic Neural Network",
        href: "/courses/lesson1",
      },
      {
        label: "DL Application for Computer Vision (CNN)",
        href: "/courses/lesson1",
      },
      {
        label: "Basic NLP",
        href: "/courses/lesson1",
      },
    ],
  },
];

export const courses = [
  {
    index: 0,
    label: "Libraries for AI Development",
    href: "/courses/ai-libraries",
  },
  {
    index: 1,
    label: "Frameworks for AI Development",
    href: "/courses/ai-frameworks",
  },
  {
    index: 2,
    label: "Introduction of Kaggle",
    href: "/courses/kaggle-introduction",
  },
  {
    index: 3,
    label:
      "Begginer to AI/ML/DL and Problem-Solving Process",
    href: "/courses/ai-ml-dl-begginer",
  },
  // {
  //   label: "Lesson 3: Linear Regression and Optimization",
  //   href: "/courses/lesson3",
  // },
  // {
  //   label:
  //     "Lesson 4: Classification Problem and Evaluation",
  //   href: "/courses/lesson4",
  // },
  // {
  //   label:
  //     "Lesson 5: Clustering and Dimensionality Reduction",
  //   href: "/courses/lesson5",
  // },
  // {
  //   label: "Lesson 6: Basic Neural Network",
  //   href: "/courses/lesson6",
  // },
  // {
  //   label:
  //     "Lesson 7: DL Application for Computer Vision (CNN)",
  //   href: "/courses/lesson7",
  // },
  // {
  //   label: "Lesson 8: Basic NLP",
  //   href: "/courses/lesson8",
  // },
  // {
  //   label:
  //     "Lesson 9: Final Project: Mini-Project Implementation + Deployment",
  //   href: "/courses/lesson9",
  // },
];
