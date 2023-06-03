import React from 'react'
import { Menu } from 'antd'
import Home from '../pages/Home';
import GrayScale from '../pages/GrayScale';
import BloodVesselSeg from '../pages/BloodVesselSeg';
import OpenCV from '../pages/OpenCV';
import Original from '../pages/Original';
import { Route, Routes, useNavigate } from 'react-router-dom';
import { HomeOutlined , DashboardOutlined, UnorderedListOutlined, UserOutlined, PoweroffOutlined} from '@ant-design/icons';

const Sidebar = () => {
  const navigate = useNavigate();
  return ( 
     <div className=" inline-flex flex-row"  >
      <Menu 
      onClick={({key}) => {
        navigate(key);
      }}
      items={[
        {label:'Home', key:"/sidebar",  icon: <HomeOutlined />},
        {label:'Gray scale', key:"/sidebar/grayscale", icon: <DashboardOutlined />},
        {label:'Blood vessel segmentation',key:"/sidebar/bloodvesselseg", icon: <UnorderedListOutlined />, danger: true},
        {label:'OpenCV', key:"/sidebar/opencv", icon: <UserOutlined />},
        {label:'Original', key:"/sidebar/original", icon: <PoweroffOutlined />}
      ]}>
      </Menu>
      {/* <Content /> */}
    </div>
  );
}

// const Content = () => {

 
//   return(
//     <div >
//       <Routes>
//         <Route path="/" element={<Home />}></Route>
//         <Route path="/grayscale" element={<GrayScale />}></Route>
//         <Route path="/bloodvesselseg" element={<BloodVesselSeg />}></Route>
//         <Route path="/opencv" element={<OpenCV />}></Route>
//         <Route path="/original" element={<Original />}></Route>
//       </Routes>
//     </div>
//   )
// }

export default Sidebar
