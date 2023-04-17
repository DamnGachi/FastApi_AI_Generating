import { Button, Form, Modal } from "react-bootstrap"

interface CreateTypeProps {
    show: boolean;
    onHide: () => void;
}

const CreateType = ({ show, onHide }: CreateTypeProps) => {
    return (
        <Modal show={show}
            onHide={onHide}
            size="lg"
            centered
        >
            <Modal.Header closeButton>
                <Modal.Title id="contained-modal-title-vcenter">
                    Add Type
                </Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <Form>
                    <Form.Control placeholder={"Input"} />
                </Form>
            </Modal.Body>
            <Modal.Footer>
                <Button variant="outline-danger" onClick={onHide}>Close</Button>
                <Button variant="outline-success" onClick={onHide}>Add</Button>
            </Modal.Footer>
        </Modal>
    )
}

export default CreateType;
