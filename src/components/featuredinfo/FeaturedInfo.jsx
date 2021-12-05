
  
import "./featuredInfo.css";
import { ArrowDownward, ArrowUpward } from "@material-ui/icons";

export default function FeaturedInfo() {
  return (
    <div className="featured">
      <div className="featuredItem">
        <span className="featuredTitle">Данные</span>
        <div className="featuredMoneyContainer">
          <span className="featuredMoney">число</span>
          <span className="featuredMoneyRate">
          </span>
        </div>
      
      </div>
      <div className="featuredItem">
        <span className="featuredTitle">Данные</span>
        <div className="featuredMoneyContainer">
          <span className="featuredMoney">число</span>
          <span className="featuredMoneyRate">
          </span>
        </div>
       
      </div>

    </div>
  );
}
