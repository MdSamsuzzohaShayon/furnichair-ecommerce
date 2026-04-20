export interface ContactBaseInterface {
    name: string;
    email: string;
    message: string;
}

export interface WillContactInterface extends ContactBaseInterface {}

export interface ContactFetchedInterface extends ContactBaseInterface{
    id: number;
    created_at: string;
    updated_at: string;
}
