import React from "react";
import { newdata } from "./../components/chart/file";
import Chart from "../components/chart/Chart";
import FeaturedInfo from "../components/featuredinfo/FeaturedInfo";
import { Link } from "react-router-dom";
import home from './home.css'



const Results = () => {
  return (
    <div>
      <h1>Результаты анализа данных</h1>
      <hr/>
      <FeaturedInfo />
      <Chart
        data={newdata}
        title="Данные о тюленях"
        grid
        dataKey="Seal Maximum"
      />

<Link to="/"> 	<button class="button button--mimas"><span>Обновить данные</span></button></Link>

    </div>
  );
};

export default Results;

