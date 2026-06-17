function isoToDate(isoString: string) {
    const formattedDate = new Date(isoString).toLocaleDateString('en-GB', { day: '2-digit', month: '2-digit', year: '2-digit' }).replace(/\//g, '/');
    return formattedDate;
}

export {
    isoToDate
}
