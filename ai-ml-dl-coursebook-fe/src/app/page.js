import React from "react";
import { homeMenu } from "@/lib/menu";

export default function page() {
  return (
    <div className="flex flex-col min-h-full">
      <section
        className="h-fit bg-white w-full
        flex flex-col justify-center items-center p-4 lg:p-[10%]
        text-black text-center font-gamja-flower border-b-2"
      >
        <h2 className="text-[50px] font-bold ">
          Artificial Intelligence - Machine Learning - Deep
          Learning English Course Book of ixxmmivsdrgn
        </h2>
        <p className="text-[30px]">
          Knowledge is summarized from Kaggle, Code Dream
          course materials, and other reference documents.
        </p>
      </section>

      {/* <div className="w-full overflow-hidden p-4">
        {homeMenu.map((item, index) => (
          <div key={index} className="p-3 w-full">
            <div className="flex justify-between items-center gap-3">
              <h4 className="text-[40px]">{item.title}</h4>
            </div>

            <div className="flex items-center justify-start gap-3 max-w-full h-fit overflow-auto">
              {item.subMenu.map((btn, idx) => (
                <button
                  key={idx}
                  className="text-[25px] px-4 w-fit h-full border-2 rounded-xl"
                >
                  {btn.label}
                </button>
              ))}
              <button className="text-[25px] px-4 w-fit h-[100px] border-2 rounded-xl">
                View all
              </button>
            </div>
          </div>
        ))}
      </div> */}
    </div>
  );
}
