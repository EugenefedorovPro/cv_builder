import React from "react";
import {ListGroup, ListGroupItem} from "react-bootstrap";
import {useFetchData} from "../api/UseFetchData";

interface BlockNamesInterface {
    experience_name: string;
    company_title: string;
    exp_period_title: string;
    position_title: string;
    achievements_title: string;
}

interface ExperienceItemInterface {
    id: number;
    company: string;
    position: string;
    start_date: string;
    end_date?: string;
    achievements: string;

}

interface ExperienceBlockInterface {
    experience: ExperienceItemInterface[];
    block_names: BlockNamesInterface;

}

const ExperienceCV = () => {
    const name = "Experience"
    const url: string = "http://localhost:8002/experience/";
    const {data, loading, error} = useFetchData<ExperienceBlockInterface>(url);

    if (loading) {
        return <div> Loading data for {name}...</div>
    }

    if (error) {
        return <div>`Error on fetching {name}: ${error}`</div>

    }

    if (!data) {
        return <div>No data on {name}</div>

    }

    const {experience, block_names} = data;

    if (!experience || !block_names) {
        return <div>No data on {name}</div>

    }


    return (
        <>
            <ListGroup>
                <ListGroupItem className="block-name">{block_names.experience_name}</ListGroupItem>
            </ListGroup>

            <ListGroup>
                {
                    experience.map((item) => (
                        <ListGroupItem className="experience-items">
                            <span className="title">{item.company}</span><br/>
                            <ul>
                                <li>
                                    <span
                                        className="title">{block_names.exp_period_title}</span> {item.start_date} - {item.end_date ? item.end_date : "current"}<br/>
                                </li>
                                <li>
                                    <span className="title">{block_names.position_title}</span> {item.position}<br/>
                                </li>
                                <li>
                                    <span className="title">{block_names.achievements_title}</span><br/>
                                    <span>{item.achievements}</span>
                                </li>
                            </ul>
                        </ListGroupItem>
                    ))
                }
            </ListGroup>
        </>

    )
}


export default ExperienceCV;
