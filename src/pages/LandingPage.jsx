import React from 'react'
import Navbar from '../components/Navbar';
import Home from './Home';
import Input from './Input';
import About from './About';
import Hero from './Hero';

const LandingPage = () => {
  return (
    <div>
      <Navbar />
      <Hero />
      <Home />
      <About />
      <Input />
    </div>
  )
}

export default LandingPage
