import React from 'react'
import { Link } from 'react-scroll'

import { NavLink, useLocation, useHistory } from 'react-router-dom';
import * as Scroll from 'react-scroll';


const Navbar = () => {
    return (

        <div className="navbar bg-base-100 sticky top-0 z-10  backdrop-filter backdrop-blur-lg bg-opacity-50 border-b border-gray-200">
            <div className="navbar-start">
                <div className="dropdown">
                    <label tabIndex={0} className="btn btn-ghost lg:hidden">
                        <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M4 6h16M4 12h8m-8 6h16" /></svg>
                    </label>
                    <ul tabIndex={0} className="menu menu-compact dropdown-content mt-3 p-2 shadow bg-base-100 rounded-box w-52">
                        
                        <li><Link to="about" spy={true} smooth={true} offset={50} duration={500}>About</Link></li>
                        <li><Link to="hero" spy={true} smooth={true} offset={50} duration={500}>Model</Link></li>
                        <li><Link to="input" spy={true} smooth={true} offset={50} duration={500}>Input</Link></li>
                        <li><Link to="team" spy={true} smooth={true} offset={50} duration={500}>Our Team</Link></li>

                        {/* <li><a>About</a></li>
                        <li><a>Model</a></li>
                        <li><a>Input</a></li>
                        <li><a>Our Team</a></li> */}
                    </ul>
                </div>
                <a className="btn btn-ghost normal-case text-xl">oculight</a>
            </div>
            <div className="navbar-center hidden lg:flex">
                <ul className="menu menu-horizontal px-1">
                    {/* <li><a>About</a></li>
                    <li><a>Model</a></li>
                    <li><a>Input</a></li>
                    <li><a>Our Team</a></li> */}

                    <li><Link to="about" spy={true} smooth={true} offset={50} duration={500}>About</Link></li>
                        <li><Link to="hero" spy={true} smooth={true} offset={50} duration={500}>Model</Link></li>
                        <li><Link to="input" spy={true} smooth={true} offset={50} duration={500}>Input</Link></li>
                        <li><Link to="team" spy={true} smooth={true} offset={50} duration={500}>Our Team</Link></li>    
                </ul>
            </div>
            <div className="navbar-end">
                <a className="btn">Get started</a>
            </div>
        </div>


        //         <div className="navbar bg-base-100 fixed top-0 z-10  backdrop-filter backdrop-blur-lg bg-opacity-50 border-b border-gray-200">
        //   <div className="flex-1">
        //     <Link to="hero" spy={true} smooth={true} offset={50} duration={500} className="btn btn-ghost normal-case text-xl" >oculight</Link>
        //   </div>
        //   <div className="flex-none">
        //     <ul className="menu menu-horizontal px-1">
        //       <li><Link to="home" spy={true} smooth={true} offset={-100} duration={500}>Home</Link></li>
        //       <li><Link to="about" spy={true} smooth={true} offset={-100} duration={500}>About</Link></li>
        //       <li><Link to="input" spy={true} smooth={true} offset={-100} duration={500}>Input</Link></li>
        //       {/* <li><Link href='#about'>About </Link></li>
        //       <li><Link href='#input'>Input</Link></li> */}

        //       {/* <li tabIndex={0}>
        //         <Link>
        //           Parent
        //           <svg className="fill-current" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24"><path d="M7.41,8.58L12,13.17L16.59,8.58L18,10L12,16L6,10L7.41,8.58Z"/></svg>
        //         </Link>
        //         <ul className="p-2 bg-base-100">
        //           <li><Link>Submenu 1</Link></li>
        //           <li><Link>Submenu 2</Link></li>
        //         </ul>
        //       </li>
        //       <li><Link>Item 3</Link></li> */}
        //     </ul>
        //   </div>
        // </div>

    )
}

export default Navbar

