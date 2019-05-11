<?php

namespace MountainTales\Packing\Model;

use Magento\Framework\Model\AbstractModel;
use MountainTales\Packing\Api\Data\StoreViewInterface;
use MountainTales\Packing\Model\ResourceModel\StoreView as StoreViewResource;

/**
 * Class StoreView
 *
 * @package   MountainTales\Packing\Model
 * @author    Jaep Cuperus <jaep@mountain-it.nl>
 * @copyright 24-4-19
 * @license   https://www.mountain-it.nl Commercial License
 */
class StoreView extends AbstractModel implements StoreViewInterface
{
    /**
     * StoreView constructor
     */
    protected function _construct()
    {
        $this->_init(StoreViewResource::class);
    }
}