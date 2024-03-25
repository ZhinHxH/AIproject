import { useState } from 'react'
import './App.css'
import { post } from './services/serivices';

function App() {

  const [links, setLinks] = useState("");

  const submitLink = async() => {
    const data = {
      url: links
    }
    const respuestas = await post("/cosa", data);
    console.log(respuestas)
  }

  return (
    <section className='page-section'>
      <div>
        <h1 className="text-center">LINK SCRIBE AI PROJECT J-J</h1>
        <article className='page-consult'>
          <input className='input-links' onChange={(e) => setLinks(e.target.value)}/>
          <button onClick={submitLink}>Send Link to ScribeAI</button>
        </article>
      </div>
      <div className='results-container'>
        Space for the table of results
      </div>
    </section>
  )
}

export default App
