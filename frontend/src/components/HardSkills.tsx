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
    const name = "Hard Skills"
    const url: string = "http://localhost:8002/hard_skills/";
    const {data, loading, error} = useFetchData<HardSkillType>(url);

    if (loading) {
        return <div> Loading data for {name}...</div>
    }

    if (error) {
        return <div>`Error on fetching {name}: ${error}`</div>

    }

    if (!data) {
        return <div>No data on {name}</div>

    }

    const [block_name, block_data] = data;

    return (
        <ListGroup>
            <ListGroupItem className="accent">{block_name.block_name}</ListGroupItem>
            {
                block_data.map((item) => (
                        <ListGroupItem key={item.id} className="">
                            <b>{item.category}</b>: {item.hard_skill_text}
                        </ListGroupItem>
                    )
                )
            }
        </ListGroup>
    )
}

export default HardSkillsCV;