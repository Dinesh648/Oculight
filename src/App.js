import logo from './logo.svg';
import './App.css';
import { Route, Routes } from 'react-router-dom';

import Navbar from './components/Navbar';
import Home from './pages/Home';
import Input from './pages/Input';
import About from './pages/About';
import Hero from './pages/Hero';
import Sidebar from './components/Sidebar';

import Original from './pages/Original';
import GrayScale from './pages/GrayScale';

import LandingPage from './pages/LandingPage';
import SidebarLayout from './layouts/SidebarLayout';
import PageNotFound from './components/PageNotFound';

function App() {

  console.log(window.location);

  return (
    <>
      {/* <Navbar /> */}
      <div className="App">
        {/* <Routes>
          <Route path='/' element={<Hero />} />
          <Route path='/home' element={<Home />} />
          <Route path='/about' element={<About />} />
          <Route path='/input' element={<Input />} />
        </Routes> */}


        {/*  mahendra */}
        <Routes >
          <Route path='/' element={<LandingPage />} />
          {/* <Route path='/sidebar' element={<Sidebar />}/>
          <Route path='/sidebar/home' element={<Home />}/>
          <Route path='/sidebar/original' element={<h1>Original image</h1>}/>
          <Route path='/sidebar/grayscale' element={<GrayScale />}/>
          <Route path='/sidebar/opencv' element={<h1>OpenCV image</h1>}/>
          <Route path='/sidebar/bloodvesselseg' element={<h1>Blood vessel segmentation image</h1>}/> */}
          <Route element={<SidebarLayout />}>
          <Route path='/sidebar' element={<Home />}/>
          <Route path='/sidebar/original' element={<h1>Original image</h1>}/>
          <Route path='/sidebar/grayscale' element={<GrayScale />}/>
          <Route path='/sidebar/opencv' element={<h1>OpenCV image</h1>}/>
          <Route path='/sidebar/bloodvesselseg' element={<h1>Blood vessel segmentation image</h1>}/> 
          </Route>
          <Route path='*' element={<PageNotFound />}/>
        </Routes>
        {/* <Hero />
        <Home />
        <About />
        <Input /> */}
        {/* <Sidebar /> */}

      </div>

    </>

  );
}

export default App;

 // let component

  // switch (window.location.pathname) {
  //   case "/":
  //     component = <Home />
  //     break;

  //   case "/about":
  //     component = <About />
  //     break;

  //   case "/input":
  //     component = <Input />
  //     break;

  //   case "/hero":
  //     component = <Hero />
  //     break;

  //   default:
  //     break;
  // }

  // {component}