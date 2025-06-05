import React from "react";
import {ListGroup, ListGroupItem} from "react-bootstrap";
import {useFetchData} from "../api/UseFetchData";

type BlockNameObject = {
    block_name: string;
}

interface InterestItemInterface {
    id: number;
    interest_text: string;

}

const InterestCV = () => {
    const name = "Interests"
    const url: string = "http://localhost:8002/interest/";
    const {data, loading, error} = useFetchData<[BlockNameObject, InterestItemInterface[]]>(url);

    if (loading) {
        return <div> Loading data for {name}...</div>
    }

    if (error) {
        return <div>`Error on fetching {name}: ${error}`</div>

    }

    if (!data) {
        return <div>No data on {name}</div>

    }

    const [block_name, data_interest] = data;

    return (
        <>
            <ListGroup>
                <ListGroupItem className="accent">{block_name.block_name}</ListGroupItem>
            </ListGroup>

            <ListGroup>
                <ListGroupItem>
                    {
                        data_interest.map((item, index) => (
                            <span key={item.id}>
                                {item.interest_text}
                                {index < data_interest.length - 1 ? ", " : ""}
                            </span>
                        ))
                    }
                </ListGroupItem>
            </ListGroup>
        </>

    )
}


export default InterestCV;
