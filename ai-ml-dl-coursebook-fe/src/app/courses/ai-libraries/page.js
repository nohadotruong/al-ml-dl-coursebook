"use client";

import React, { useState } from "react";
import { motion } from "framer-motion";
import TableOfContents from "@/app/components/TableOfContents";
import NavigateButton from "@/app/components/NavigateButton";

export default function page() {
  const [tableOpen, setTableOpen] = useState(false);
  const contents = [
    {
      title: "1. Pandas",
      href: "#pandas",
    },
    {
      title: "2. Numpy",
      href: "#numpy",
    },
    {
      title: "3. Matplotlib",
      href: "#matplotlib",
    },
    {
      title: "4. SeaBorn",
      href: "#seaborn",
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
          Libraries for AI Development
        </h2>
      </motion.section>

      <div className="w-full lg:w-[80%] px-4 mx-auto">
        <NavigateButton lesson={0} />

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
          <h3 className="text-[30px] font-semibold"></h3>
          <p className="text-[25px]"></p>
        </motion.div>

        <motion.div
          initial={{ x: -100, opacity: 0 }}
          animate={{ x: 0, opacity: 1 }}
          className="p-3 flex-col gap-3 mt-3"
          id="data-science"
        >
          <h3 className="text-[30px] font-semibold"></h3>
          <div className="flex flex-col p-2 gap-2 text-[25px]"></div>
        </motion.div>

        <NavigateButton lesson={0} />
      </div>
    </div>
  );
}
