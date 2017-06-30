import { AcvariuPage } from './app.po';

describe('acvariu App', () => {
  let page: AcvariuPage;

  beforeEach(() => {
    page = new AcvariuPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
