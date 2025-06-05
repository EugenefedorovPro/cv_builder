import React from "react";
import {ListGroup, ListGroupItem} from "react-bootstrap";
import {useFetchData} from "../api/UseFetchData";

type BlockNameObject = {
    block_name: string;
}

interface ExperienceItemInterface {
    id: number;
    company: string;
    position: string;
    start_date: string;
    end_date?: string;
    achievements: string;

}

const ExperienceCV = () => {
    const url: string = "http://localhost:8002/experience/";
    const {data, loading, error} = useFetchData<[BlockNameObject, ExperienceItemInterface[]]>(url);

    if (loading) {
        return <div> Loading data for Hard Skills...</div>
    }

    if (error) {
        return <div>`Error on fetching Hard Skills: ${error}`</div>

    }

    if (!data) {
        return <div>No data on Experience</div>

    }

    const [block_name, data_experience] = data;

    return (
        <>
            <ListGroup>
                <ListGroupItem className="accent">{block_name.block_name}</ListGroupItem>
            </ListGroup>

            <ListGroup>
                {
                    data_experience.map((item) => (
                        <ListGroupItem>
                            <b>Company</b> {item.company}<br/>
                            <b>Period</b> {item.start_date} - {item.end_date}<br/>
                            <b>Position</b> {item.position}<br/>
                            <b>Achievements</b><br/>
                            <span>{item.achievements}</span>
                        </ListGroupItem>
                    ))
                }
            </ListGroup>
        </>

    )
}


export default ExperienceCV;
