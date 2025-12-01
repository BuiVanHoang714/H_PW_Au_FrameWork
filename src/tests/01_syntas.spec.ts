import { test, expect } from '@playwright/test';

test.describe('Homepage - Material PlaywrightVN', () => {
  
  test('should display correct page title', async ({ page }) => {
    await page.goto('https://material.playwrightvn.com/');
    await expect(page).toHaveTitle(/Tài liệu học automation test/);
  });
  
  test('should navigate to Register Page lesson', async ({ page }) => {
    await page.goto('https://material.playwrightvn.com/');
    await page.getByRole('link', { name: 'Bài học 1: Register Page' }).click();
    await expect(page.getByRole('heading', { name: 'User Registration' })).toBeVisible();
  });

  test('')
  
});