import React from "react";
import { urlInterest } from "../urls";
import {ListGroup, ListGroupItem} from "react-bootstrap";
import {useFetchData} from "../api/UseFetchData";

interface BlockNameInterface {
    interest_name: string;
}

interface InterestItemInterface {
    id: number;
    interest_text: string;

}

interface InterestBlockInterface {
    interests: InterestItemInterface[];
    block_names: BlockNameInterface;
}

const InterestCV = () => {
    const name = "Interests"
    const {data, loading, error} = useFetchData<InterestBlockInterface>(urlInterest);

    if (loading) {
        return <div> Loading data for {name}...</div>
    }

    if (error) {
        return <div>`Error on fetching {name}: ${error}`</div>

    }

    if (!data) {
        return <div>No data on {name}</div>

    }

    const {interests, block_names} = data;

    return (
        <>
            <ListGroup>
                <ListGroupItem className="block-name">{block_names.interest_name}</ListGroupItem>
            </ListGroup>

            <ListGroup>
                <ListGroupItem className="interests-items">
                    {
                        interests.map((item, index) => (
                            <span key={item.id}>
                                {item.interest_text}
                                {index < interests.length - 1 ? " • " : ""}
                            </span>
                        ))
                    }
                </ListGroupItem>
            </ListGroup>
        </>

    )
}


export default InterestCV;
