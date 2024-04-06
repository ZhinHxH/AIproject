import { useState, useEffect } from 'react'
import { post, get } from './services/serivices';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import './App.css'

function App() {

  const [links, setLinks] = useState("");
  const [entity, setEntity] = useState([]);
  const [act, setact] = useState(false);

  useEffect(() => {
    getAll()
  }, [act]);


  const getAll = async()  => {
    const respuestas = await get("/identifyUrl")
    setEntity(respuestas)
  }

  const submitLink = async() => {
    const data = {
      url: links,
      texto: '',
      clasificacion: ''
    }

    const respuestas = await post("/identifyUrl", data);
    if(respuestas){
      setact(!act)
    }
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
        <TableContainer component={Paper}>
          <Table sx={{ minWidth: 650 }} aria-label="simple table">
            <TableHead>
              <TableRow>
                <TableCell>ENLACE</TableCell>
                <TableCell>TEXTO</TableCell>
                <TableCell>CLASIFICACION</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {entity ? (<>
                {entity.map((row)=>(<>
                  <TableRow key={row.ID}>
                    <TableCell>{row.URL}</TableCell>
                    <TableCell>{row.TEXTO}</TableCell>
                    <TableCell>{row.CLASIFICACION}</TableCell>
                  </TableRow>
                </>))}
              </>): null}
            </TableBody>
          </Table>
        </TableContainer>      
      </div>
    </section>
  )
}

export default App
