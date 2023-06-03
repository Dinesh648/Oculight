import React from 'react'
import Sidebar from '../components/Sidebar'
import { Outlet } from 'react-router-dom'

const SidebarLayout = () => {
  return (
    <main className=''>
        <Sidebar />
        <div className=' inline-flex '>
            <Outlet />
        </div>
    </main>
  )
}

export default SidebarLayout
