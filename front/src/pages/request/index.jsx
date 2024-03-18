"use client"
import {useEffect, useState} from "react";
import httpClient from "@/services/httpClient";
import {Button, Modal, Table} from "flowbite-react";

export default function Request() {
    const [isLogged, setIsLogged] = useState(null)
    const [requests, setRequests] = useState([])
    const [selectedRequest, setSelectedRequest] = useState(null)
    const [decisionDetail, setDecisionDetail] = useState(null)
    const [openModal, setOpenModal] = useState(false);

    useEffect(() => {
        setIsLogged(sessionStorage.getItem('token')?.length > 0)
        try {
            httpClient.get('requests')
                .then((value) => {
                    setRequests(value)
                })
        } catch (e) {
            console.log("error recuperation requests", e)
        }

    }, []);

    const handleButtonClick = async (requestId) => {
        setDecisionDetail(null)
        const value = await httpClient.get(`/decision/request/${requestId}`)
        setOpenModal(true)
        setDecisionDetail(value)
    }
    return (
        <>
            <div>
                Dashboard pour voir les prets
            </div>
            <div>
                Mes demandes
                <Table striped>
                    <Table.Head>
                        <Table.HeadCell>Id</Table.HeadCell>
                        <Table.HeadCell>Text</Table.HeadCell>
                        <Table.HeadCell>Status</Table.HeadCell>
                        <Table.HeadCell>Date</Table.HeadCell>
                        <Table.HeadCell>
                            <span className="sr-only">Voir le detail</span>
                        </Table.HeadCell>
                    </Table.Head>
                    <Table.Body className="divide-y">
                        {requests.map((request) => (
                            <Table.Row className="bg-white dark:border-gray-700 dark:bg-gray-800" key={request?.id}>
                                <Table.Cell>{request?.id}</Table.Cell>
                                <Table.Cell>{request?.text}</Table.Cell>
                                <Table.Cell>{request?.status}</Table.Cell>
                                <Table.Cell>{request?.created_at}</Table.Cell>
                                <Table.Cell>
                                    <Button onClick={() => handleButtonClick(request?.id)}>Voir le detail</Button>
                                </Table.Cell>
                            </Table.Row>
                        ))}
                    </Table.Body>
                </Table>
                <Modal dismissible show={openModal} onClose={() => setOpenModal(false)}>
                    <Modal.Header>Demande detail</Modal.Header>
                    <Modal.Body>
                        <div className="space-y-6">
                            <div className="flex flex-col space-y-1">
                                <span className="font-semibold">Décision:</span>
                                <p className="text-base leading-relaxed text-gray-700 dark:text-gray-400">{decisionDetail?.decision}</p>
                            </div>
                            <div className="flex flex-col space-y-1">
                                <span className="font-semibold">Message:</span>
                                <p className="text-base leading-relaxed text-gray-700 dark:text-gray-400">{decisionDetail?.message}</p>
                            </div>
                            <div className="flex flex-col space-y-1">
                                <span className="font-semibold">Montant mensuel:</span>
                                <p className="text-base leading-relaxed text-gray-700 dark:text-gray-400">{decisionDetail?.monthly_amount}</p>
                            </div>
                            <div className="flex flex-col space-y-1">
                                <span className="font-semibold">Taux d'intérêt:</span>
                                <p className="text-base leading-relaxed text-gray-700 dark:text-gray-400">{decisionDetail?.interest_rate}</p>
                            </div>
                            <div className="flex flex-col space-y-1">
                                <span className="font-semibold">Détails de la décision:</span>
                                <p className="text-base leading-relaxed text-gray-700 dark:text-gray-400">{decisionDetail?.reason}</p>
                            </div>
                        </div>
                    </Modal.Body>
                    <Modal.Footer>
                        <Button onClick={() => setOpenModal(false)}>Fermer</Button>
                    </Modal.Footer>
                </Modal>
            </div>

        </>
    )
}