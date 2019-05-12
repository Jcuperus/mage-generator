/**
 * {@inheritDoc}
 */
public function getStoreViewId()
{
    return $this->getData(self::STORE_VIEW_ID);
}

/**
 * {@inheritDoc}
 */
public function setStoreViewId($storeViewId)
{
    return $this->setData(self::STORE_VIEW_ID, $storeViewId);
}