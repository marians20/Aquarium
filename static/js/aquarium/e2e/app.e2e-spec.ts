import { AquariumPage } from './app.po';

describe('aquarium App', () => {
  let page: AquariumPage;

  beforeEach(() => {
    page = new AquariumPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
