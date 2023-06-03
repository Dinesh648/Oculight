// import React from 'react'

// const Home = () => {
//   return (
//     <div>
//       <h1>Home</h1>
      
//     </div>
//   )
// }

// export default Home

import React from 'react';
import * as Scroll from 'react-scroll';

export default function Home() {
  const Element = Scroll.Element;

  return (
    <div id='home'>
      <h1 className='text-9xl'>Home</h1>
      <p className='text-6xl'>Welcome</p>
      <p>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed gravida
        fermentum purus egestas blandit. Nam nisl sem, feugiat hendrerit magna
        non, ullamcorper pharetra nibh. Sed vestibulum nisi enim, non bibendum
        lorem aliquam non. Cras turpis risus, elementum a sapien quis, dictum...
      </p>
      <p>
        Sed volutpat, turpis vitae cursus viverra, quam tortor maximus felis,
        tempus eleifend nulla metus et sapien. Curabitur vitae sodales dolor.
        Phasellus a ultrices felis. Aenean efficitur nibh sit amet tortor...
      </p>
      <Element name="anchor">
        Nam nisi nisi, aliquet at blandit et, pulvinar sit amet quam. Sed
        euismod ex dui, posuere tristique purus tincidunt in. Orci varius
        natoque penatibus et magnis dis parturient montes, nascetur ridiculus
        mus. Vestibulum sit amet nisi commodo, pretium quam non, scelerisque...
      </Element>
    </div>
  );
}
