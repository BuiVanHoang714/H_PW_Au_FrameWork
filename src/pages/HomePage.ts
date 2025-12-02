import { Page, expect } from "@playwright/test";
import BasePage from "./BasePage";

export default class Homepage extends BasePage{

    private readonly serviceTitleLocator = "Service"
   

    constructor (page : Page){
        super(page);
        
    }

    async expectedServiceTitleToBeVisible(){
        await expect(this.page.getByTitle(this.serviceTitleLocator)).toBeVisible({ timeout : 15000});
    }
}