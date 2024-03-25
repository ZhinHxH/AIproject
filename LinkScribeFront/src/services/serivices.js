// This is an file for the request configuration for the rest api
// Firts we declare the global variable wiht the url of the api
const backendUrl = '';

// Build a function for tramit the GET querys
export const get = async (url) => {
    try {
        const response =  await fetch(`${backendUrl}${url}`);
        if(response.status === 200) {
            const data = await response.json();
            return data;
        }
    }
    catch (error) {
        console.log('Error to tramit the petition GET: ', error);
        throw error;
    }
}

// For the POST method
export const post = async(url, body) =>{
    try {
        const requestOptions = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(body),
        };

        const response =  await fetch(`${backendUrl}${url}`, requestOptions);
        if(response.status === 200) {
            const data = await response.json();
            return data;
        }
    }
    catch (error) {
        console.log('Error to tramit the petition POST: ', error);
        throw error;
    }
}

// DELETE method
export const remove = async (url) => {
    try {
        const response = await fetch(`${backendUrl}${url}`, {
        method: 'DELETE',
        });
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error al realizar la solicitud DELETE:', error);
        throw error;
    }
};