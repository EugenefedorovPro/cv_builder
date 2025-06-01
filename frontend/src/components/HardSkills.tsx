import React from "react";
import {useFetchData} from "../api/UseFetchData";
import {ListGroup, ListGroupItem, Container} from "react-bootstrap";


type BlockNameObject = {
    block_name: string,
}

interface HardSkillsItemInterface {
    id: number,
    category: string,
    hard_skill_text: string,
}

type HardSkillType = [
    BlockNameObject,
    HardSkillsItemInterface[],
]

const HardSkillsCV = () => {
    const url: string = "http://localhost:8002/hard_skills/";
    const {data, loading, error} = useFetchData<HardSkillType>(url);


    console.log(data);

    if (loading) {
        return <div> Loading data for Hard Skills...</div>
    }

    if (error) {
        return <div>`Error on fetching Hard Skills: ${error}`</div>

    }

    if (!data) {
        return <div>No data on Hard Skills</div>

    }

    const [block_name, block_data] = data;

    return (
        <ListGroup>
            <ListGroupItem className="fw-bold">{block_name.block_name}</ListGroupItem>
            <ListGroupItem>
                {
                    block_data.map((item) => (
                            <ListGroup>
                                <ListGroupItem className=""><b>{item.category}</b>: {item.hard_skill_text}</ListGroupItem>
                            </ListGroup>
                        )
                    )
                }
            </ListGroupItem>

        </ListGroup>
    )
}

export default HardSkillsCV;