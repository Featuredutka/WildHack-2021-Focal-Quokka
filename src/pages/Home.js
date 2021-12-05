import React from "react";
import { Link } from "react-router-dom";
import home from './home.css'


const Home = () => {

 const runPython =()=>{
  let first = 10;
  let second = 20;
  window.open('http://10.211.55.3:80/add')
  return
}
  return (
   <div>
    <div className='header'>
    <img src='http://kronoki.ru/kronoki-ru-250.png' alt=''/>
    </div>
    <h1>Мониторинг популяции тюленей на территории Кроноцкого заповедника</h1>
    <div className='wrapper'>
					<button onClick={runPython} class="button button--mimas"><span>Анализ фотографий</span></button>
     
      <Link to="/results"> <button class="button button--mimas"><span>Анализ данных</span></button></Link>
    </div>
    <div className='footer'>
     </div>
    </div>
  );
};

export default Home;
