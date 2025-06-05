import React from "react";
import {ListGroup, ListGroupItem} from "react-bootstrap";
import {useFetchData} from "../api/UseFetchData";

type BlockNameObject = {
    block_name: string;
}

interface NaturalLangItemInterface {
    id: number;
    natural_lang: string;
    level: string;

}

const NaturalLangCV = () => {
    const name = "Natural languages"
    const url: string = "http://localhost:8002/natural_lang/";
    const {data, loading, error} = useFetchData<[BlockNameObject, NaturalLangItemInterface[]]>(url);

    if (loading) {
        return <div> Loading data for {name}...</div>
    }

    if (error) {
        return <div>`Error on fetching {name}: ${error}`</div>

    }

    if (!data) {
        return <div>No data on {name}</div>

    }

    const [block_name, data_natural_lang] = data;

    return (
        <>
            <ListGroup>
                <ListGroupItem className="accent">{block_name.block_name}</ListGroupItem>
            </ListGroup>

            <ListGroup>
                <ListGroupItem>
                    {
                        data_natural_lang.map((item, index) => (
                            <span key={item.id}>
                                <b>{item.natural_lang}</b> - {item.level}
                                {index < data_natural_lang.length - 1 ? ", " : ""}
                            </span>
                        ))
                    }
                </ListGroupItem>
            </ListGroup>
        </>

    )
}


export default NaturalLangCV;
