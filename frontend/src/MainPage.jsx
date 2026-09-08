import { useState, useEffect  } from "react"

function MainPage() {

    const [data, setData] = useState({})

    useEffect(() => {
        const fetchData = async () => {
            try{
                const response = await fetch("http://127.0.0.1:8000/fetch_rate");

                const result = await response.json();

                setData(result)
            }
            catch (error) {
                console.error('Error Fetching data:', error)
            }
        }
        fetchData();
    }, []); 

    return (
        <>
        <div>INR to GBP Today</div>
        <div>{data ? data.rate : "Loading..."} </div>
        </>
    );

}

export default MainPage