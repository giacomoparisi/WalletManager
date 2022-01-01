export type Transaction = {
    id: string
    type: string
    description: string
    value: number
    date: string
}

export type TransactionState = {
    loading: boolean
    error: string | null
    data: Transaction[]
}
